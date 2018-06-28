from fabric.api import local, warn_only

### Maven commands:

def test():
    local("mvn test")
    testsoapui()

def test_ignore():
    local("mvn test -Dmaven.test.failure.ignore=true")
    testsoapui()

def compile():
    local("mvn compile")

def install():
    local("mvn install")

def install_test_skip():
    local("mvn install -Dmaven.test.skip=true")

def testapi():
    local("scripts\\test_abc_soap.bat")
    local("scripts\\test_abc_rest.bat")

### Dev-Run:

def echojboss():
	local("echo %JBOSS_HOME%")

def dirjboss():
	local("dir %JBOSS_HOME%\\standalone\\deployments\\")

def removewar():
	dirjboss()
	with warn_only():
		local("del %JBOSS_HOME%\\standalone\\deployments\\ABC.war")
		local("rmdir %JBOSS_HOME%\\standalone\\deployments\\ABC.war /S /Q")
		local("del %JBOSS_HOME%\\standalone\\log\\server.log")
	dirjboss()

def run():
	local("%JBOSS_HOME%\\bin\\standalone.bat")

def cleandeploy():
	install_test_skip()
	deploywar()

def cleanrun():
	cleandeploy()
	run()

def deploywar():
	removewar()
	local("scripts\\deployABC.bat")

### Script footer.

print('Done.')