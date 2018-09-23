from subprocess import Popen, PIPE

def get_snp_genotype(path, line=1):
	line += 1
	command = 'head -n %s %s | tail -1' % (line, path)
	a = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
	out, err = a.communicate()
	a.wait()
	return out