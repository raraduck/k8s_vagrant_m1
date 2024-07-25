# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  ## Hostmanager plugin
  config.hostmanager.enabled = true
  config.hostmanager.manage_guest = true
  # config.hostmanager.include_offline = true
  config.hostmanager.host_file_path = "/etc/hosts"

  config.vm.define "controlplane1" do |config0|
    config0.vm.box = "mpasternak/focal64-arm"
    config0.vm.hostname = "controlplane1"
    config0.vm.network "private_network", ip: "192.168.56.11"
    config0.vm.provider "parallels" do |prl|
      prl.name = "controlplane1"
      prl.cpus = 2
      prl.memory = 4096
      prl.customize ["set", :id, "--device-add", "net", "--type", "host-only"]
    end
    # Enable SSH Password Authentication
    config0.vm.provision "shell", inline: <<-SHELL
      sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
      systemctl restart ssh
      systemctl start systemd-timesyncd
      timedatectl set-timezone UTC
    SHELL
  end

  config.vm.define "node1" do |config1|
    config1.vm.box = "mpasternak/focal64-arm"
    config1.vm.hostname = "node1"
    config1.vm.network "private_network", ip: "192.168.56.21"
    config1.vm.provider "parallels" do |prl|
      prl.name = "node1"
      prl.cpus = 2
      prl.memory = 2048
      # prl.customize ["set", :id, "--device-del", "net0"]
      prl.customize ["set", :id, "--device-add", "net", "--type", "host-only"]
    end
    # Enable SSH Password Authentication
    config1.vm.provision "shell", inline: <<-SHELL
      sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
      systemctl restart ssh
      systemctl start systemd-timesyncd
      timedatectl set-timezone UTC
    SHELL
  end 

  config.vm.define "node2" do |config2|
    config2.vm.box = "mpasternak/focal64-arm"
    config2.vm.hostname = "node2"
    config2.vm.network "private_network", ip: "192.168.56.22"
    config2.vm.provider "parallels" do |prl|
      prl.name = "node2"
      prl.cpus = 2
      prl.memory = 2048
      # prl.customize ["set", :id, "--device-del", "net0"]
      prl.customize ["set", :id, "--device-add", "net", "--type", "host-only"]
    end
    # Enable SSH Password Authentication
    config2.vm.provision "shell", inline: <<-SHELL
      sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
      systemctl restart ssh
      systemctl start systemd-timesyncd
      timedatectl set-timezone UTC
    SHELL
  end

  config.vm.define "node3" do |config3|
    config3.vm.box = "mpasternak/focal64-arm"
    config3.vm.hostname = "node3"
    config3.vm.network "private_network", ip: "192.168.56.23"
    config3.vm.provider "parallels" do |prl|
      prl.name = "node3"
      prl.cpus = 2
      prl.memory = 2048
      # prl.customize ["set", :id, "--device-del", "net0"]
      prl.customize ["set", :id, "--device-add", "net", "--type", "host-only"]
    end
    # Enable SSH Password Authentication
    config3.vm.provision "shell", inline: <<-SHELL
      sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
      systemctl restart ssh
      systemctl start systemd-timesyncd
      timedatectl set-timezone UTC
    SHELL
  end
end
