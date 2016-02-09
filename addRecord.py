#!/usr/bin/env python

import pyrax
import os
import sys

def main():
    domain_name = sys.argv[1]
    host_name = sys.argv[2]
    ip_address = sys.argv[3]

    pyrax.set_setting("identity_type","rackspace")
    pyrax.set_credentials(os.environ['RACKSPACE_USERNAME'], os.environ['RACKSPACE_API_KEY'])

    domain = pyrax.cloud_dns.find(name=domain_name)
    record = ({"type": "A", "name": host_name, "data": ip_address, "ttl":300})

    domain.add_records(record)

if __name__ == "__main__":
    main()
