import whois 



nic_client = NICClient()

options, args = parse_command_line(sys.argv)
if options.b_quicklookup:
    flags = flags | NICClient.WHOIS_QUICK
print(nic_client.whois_lookup(options.__dict__, args[1], flags))