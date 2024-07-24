# Vagrant VM for Kubernetes Simulation on M1 with Parallels
```
vagrant up controlplane1 && vagrant up node1 && vagrant up node2 && vagrant up node3
```

## 기본 환경 구성 ( Virtualbox + Vagrant )
1. virtualbox.org 공식 홈페이지에서 다운로드
2. vagrantup.com 공식 홈페이지에서 다운로드
3. vagrant 명령어를 통해 가상머신 배포
  a. vagrant init : Vagrantfile 파일 생성
  b. vagrant plugin install vagrant-hostmanager : 플러그인 설치
  c. vagrant up : 가상머신 생성
  d. vagrant ssh VMNAME : 원격접속
  e. vagrant status : 가상머신 상태 확인
  f. vagrant halt : 가상머신 종료
  g. vagrant snapshot save NAME : 스냅샷 저장
  h. vagrant snapshot restore NAME : 되돌리기

```
kubespray 설치 가이드
https://kubernetes.io/ko/docs/setup/production-environment/tools/kubespray/

https://github.com/kubernetes-sigs/kubespray
```

### 참고: 설치 시 가상머신 정리
1.	virtualbox 목록에서 전체 삭제하기로 삭제
2.	혹은 C:/users/USERNAME/Virtualbox VMs 폴더에서 폴더 통째로 삭제하기


## kubespray 설치
### 1.깃 저장소 복사
```
$ sudo apt update
$ sudo apt install git python3 python3-pip
$ git clone --single-branch --branch=release-2.22 https://github.com/kubernetes-sigs/kubespray.git
```

### 2.의존성 패키지 설치
```
$ cd kubespray
$ pip3 install -r requirements.txt
```
### 3.인벤토리 파일 준비
```
$ cp -rfp inventory/sample inventory/mycluster  
$ vim inventory/mycluster/inventory.ini
```
### 4.ssh key 설정
```
$ ssh-keygen
$ ssh-copy-id vagrant@node1
$ ssh-copy-id vagrant@node2
$ ssh-copy-id vagrant@node3
```
## 참고 : 각 시스템에 사용자 준비 필요
- sudo 명령어 사용이 가능하도록 설정
```
sudo cat /etc/sudoers.d/vagrant
vagrant ALL=(ALL) NOPASSWD:ALL
```
### 5.설정편집
vim inventory/mycluster/group_vars/k8s_cluster/addons.yml
```
helm_enabled: true
metrics_server_enabled: true   
ingress_nginx_enabled: true
metallb_enabled: true
metallb_protocol: "layer2" (주석해제)
metallb_config:
  address_pools:
    primary:
      ip_range:
        - 192.168.56.200-192.168.56.210
      auto_assign: true
```
-> 주석 해제 및 주소 대역 수정
```
$ vim inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml
kube_proxy_strict_arp: true
```
### 6.앤서블 명령어로 확인 및 설치
```
$ ansible -m ping all -i inventory/mycluster/inventory.ini 
-> 인벤토리파일에 설정해둔 시스템이 앤서블로 작업이 가능한지 연결상태를 확인

$ ansible all -i inventory/mycluster/inventory.ini -m apt -a 'update_cache=yes' -b
-> apt (패키지) 캐시 정보 업데이트
-i : 인벤토리 파일 지정 옵션
-m : 실행할 모듈 지정 옵션
-a : 각 모듈에 대한 세부항목 지정 옵션
-b : 권한상승 옵션

$ ansible-playbook -i inventory/mycluster/inventory.ini cluster.yml -b
-> 실질적인 쿠버네티스 환경 배포 작업 시작
```

#### 설치 중 오류 발생 시 
```
ansible-playbook -i inventory/mycluster/inventory.ini cluster.yml -b --start-at-task="작업이름"
라고 입력하면 해당 위치부터 다시 이어서 시도
TASK [network_plugin/calico : Set calico_pool_conf]
에서 만약 오류 발생 시 
괄호 안 글자 전체가 작업이름입니다.
```

## 초기 명령어 사용 설정
### 1.root 사용자로 전환
```
vagrant@controlplane1:~$ sudo -i
```
### 2.인증파일 생성
```
root@controlplane1:~# mkdir ~vagrant/.kube    
root@controlplane1:~# cp /etc/kubernetes/admin.conf ~vagrant/.kube/config 
root@controlplane1:~# chown -R vagrant. ~vagrant/.kube/    
```
### 3.명령어 자동완성 (kubespray 는 기본 설정)
```
root@controlplane1:~# kubectl completion bash > /etc/bash_completion.d/kubectl
```

