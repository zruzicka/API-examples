# ABC API module #

* **This is just Readme file template for fictional ABC API module.**
* ABC API module provides both SOAP and REST APIs for manipulating with ABC entities.
* Create/Update/Deactivate/Get/Search operations are provided for Task and Category entities based on business requirements (BRs).
* Features details and BRs are listed in Jira/ABC user stories.
* This Readme provides overview of basic topics and other relevant resources for this module.

### SOAP API contract
* SOAP WSDL defines all SOAP API details as available methods, expected inputs and output structure.
* Contract file: `ABC/soap/v1/manageRoutineWork_v1.wsdl`
* High level overview provides `ABC/contracts/SOAP_API_v1_contract`

### REST API contract
* REST API contract is written in [API Blueprint](https://apiblueprint.org/) syntax. 
* Contract file: `ABC/rest/ABCv1.apib`
* Please use your favourite Markdown syntax viewer for reading `ABC/rest/ABCv1.apib`

### API response codes
* Response and status codes contract describes available API responses with status codes, messages and defines matrix between codes and API methods.
* Contract file: `ABC/contracts/API_v1_statusCodes_contract`

### ABC module tech stack
* Maven for builds and dependencies management
* Java 1.8, Spring 
* Spring for DI and RestController
* SOAP endpoint interface generated from WSDL by wsimport and JAX-WS.
* RestController based on Spring. Jackson Databind used for model (de)serialization.
* Oracle DB access via JDBC, implemented model mappers.

### ABC code setup into IDE
* Requirements:
	* Maven
	* Java 1.8
* You can import `ABCManager` as Maven project into your IDE.
* The rest of dependencies will be loaded by Maven from Maven central repo.
	
### Build and deployment
* Module build via `mvn install` command.
* `ABC/scripts/deployABC.bat` - ABC deployment into local JBoss AS.
* [Jenkins test build job for ABC dev branch](http://jenkins-hosting.com:18123/jenkins/job/dev_abc)

### ABC/API test cases
* API templates and test cases are available in following SoapUI projects
	* `ABC/soapui/ABC_SOAP_requests.xml`
	* `ABC/soapui/ABC_REST_requests.xml`
* ABC internal unit testing via jUnit.
* UAT environment testing:
	* Subset of REST tests provides `ABC/soapui/uat/ABC_REST_requests_UAT.xml`

### ABC API endpoints
API endpoints URL depends on the latest configuration. At this moment following endpoints can be used.
* Local SOAP endpoint: `http://localhost:8080/ABC/ABCSOAPController`
* Local REST endpoint: `http://localhost:8080/ABC/api/v1/`
	
### ABC internal model
* Complete Task and Category entities fields definition and values enumeration can be found in `ABC/soap/v1/RWGTypes.xsd` or in generated classes.

### API Authorization Design
* Authorization checks are performed in ABCService throught ABCAuthorization service, checked permissions and provided clientUserGroup.
* Document file: `ABC/auth/Summary notes for ABC API Authorization Design`

### ABC internal dataflow
* SOAP/REST requests are processed by ABC[SOAP|REST]Controller which use ABCService.
* ABCService uses individual Task/CategoryService and provides authorization check via ABCAuthorization.
* Task/CategoryService call DAOs.
* DAOs build queries and call JDBC. Results mapping into model via model mappers.
* Services fill ResponseTypes and StatusDetails based on DB operations results.
* Fully initialized ResponseType is returned back to controller which provides response to initial request.

### Development related scripts
* `ABC/soap/v1/generate_stub_v1.bat` - Java SOAP endpoint interface cleanup and generating via wsimport. 
* `ABC/fabfile.py` - Python script with functions for build, deployment and for removing old artifacts.
* `ABC/scripts/deployABC.bat` - ABC deployment into local JBoss AS.
* `ABC/scripts/test_ABC_rest.bat` - Executes ABC REST API test cases.
* `ABC/scripts/test_ABC_soap.bat` - Executes ABC SOAP API test cases.
