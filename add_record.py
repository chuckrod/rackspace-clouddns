#!/usr/bin/env python
"""
Script used to add Rackspace DNS Record
"""

import pyrax
import os
import sys

def main():
    """
    Main function of script
    """
    domain_name = sys.argv[1]
    host_name = sys.argv[2]
    ip_address = sys.argv[3]
    record_type = sys.argv[4]
    ttl = sys.argv[5]

    pyrax.set_setting("identity_type", "rackspace")
    pyrax.set_credentials(os.environ['RACKSPACE_USERNAME'],
			  os.environ['RACKSPACE_API_KEY'])

    domain = pyrax.cloud_dns.find(name=domain_name)
    record = ({"type": record_type, "name": host_name, "data": ip_address, "ttl":ttl})

    domain.add_records(record)

if __name__ == "__main__":
    main()
