# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "controlplane1" do |config|
    config.vm.box = "ilker/ubuntu2004"
    config.vm.box_version = "1.0"
    # config.vm.box = "arm64v8/ubuntu:20.04"
    config.vm.hostname = "controlplane1"
    config.vm.network "private_network", ip: "192.168.56.11"
    config.vm.provider "parallels" do |vb|
      vb.name = "controlplane1"
      vb.cpus = 2
      vb.memory = 4096
    end
  end
  config.vm.define "node1" do |config|
    config.vm.box = "ilker/ubuntu2004"
    config.vm.box_version = "1.0"
    # config.vm.box = "arm64v8/ubuntu:20.04"
    config.vm.provider "parallels" do |vb|
      vb.name = "node1"
      vb.cpus = 2
      vb.memory = 2048
    end
    config.vm.hostname = "node1"
    config.vm.network "private_network", ip: "192.168.56.21"
  end
  config.vm.define "node2" do |config|
    config.vm.box = "ilker/ubuntu2004"
    config.vm.box_version = "1.0"
    # config.vm.box = "arm64v8/ubuntu:20.04"
    config.vm.provider "parallels" do |vb|
      vb.name = "node2"
      vb.cpus = 2
      vb.memory = 2048
    end
    config.vm.hostname = "node2"
    config.vm.network "private_network", ip: "192.168.56.22"
  end
  config.vm.define "node3" do |config|
    config.vm.box = "ilker/ubuntu2004"
    config.vm.box_version = "1.0"
    # config.vm.box = "arm64v8/ubuntu:20.04"
    config.vm.provider "parallels" do |vb|
      vb.name = "node3"
      vb.cpus = 2
      vb.memory = 2048
    end
    config.vm.hostname = "node3"
    config.vm.network "private_network", ip: "192.168.56.23"
  end

  # Hostmanager plugin
  config.hostmanager.enabled = true
  config.hostmanager.manage_guest = true

  # Enable SSH Password Authentication
  config.vm.provision "shell", inline: <<-SHELL
    swapoff -a
    sed -i '/swap/s/^/#/' /etc/fstab
    sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
    # sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
    # sed -i 's/security.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
    systemctl restart ssh
    systemctl start systemd-timesyncd
    timedatectl set-timezone UTC
  SHELL
end

