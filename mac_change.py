import optparse,subprocess

def arguments():
	parse = optparse.OptionParser()
	parse.add_option("-i", "--interface", dest="interface", help="Interface para alterar endereco MAC")
	parse.add_option("-m", "--mac", dest="mac", help="Novo endereco MAC")
	return parse.parse_args()
def mac_change(interface, mac):
	subprocess.call(["ifconfig", interface,"down"])
	subprocess.call(["ifconfig", interface,"hw","ether",mac])
	subprocess.call(["ifconfig", interface, "up"])
	print "[+] Mundando endereco MAC de %s para %s" % (interface, mac)

opt, argv = arguments()
mac_change(opt.interface, opt.mac)


