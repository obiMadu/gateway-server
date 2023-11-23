#create gate-vpc
resource "digitalocean_vpc" "gate_vpc" {
  name     = "gate-vpc"
  region   = var.do_region
  ip_range = "10.10.10.0/24"
}

#create gate droplet
resource "digitalocean_droplet" "gate" {
  name     = "gate2"
  size     = "s-1vcpu-1gb"
  image    = "ubuntu-22-04-x64"
  region   = var.do_region
  vpc_uuid = digitalocean_vpc.gate_vpc.id
  backups = true
  monitoring = true
  user_data = file("../userdata.yml")
}

#create reserved-ip for gate
resource "digitalocean_reserved_ip" "r_ipv4" {
  droplet_id = digitalocean_droplet.gate.id
  region     = digitalocean_droplet.gate.region
}