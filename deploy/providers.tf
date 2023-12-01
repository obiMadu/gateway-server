terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
  backend "gcs" {
    bucket = "lsdkfk-gateway-server-do-prod"
    prefix = "terraform/state"
  }
}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.do_token
}