from subprocess import call

def main():
	
	print "Testing connectivity\n"
	call(["ping","-c 2","localhost"])
	print "\n"

	print "Listing all containers\n"
	call(["curl", "-s","-X GET","-H 'Accept:application/json'","localhost:8080/containers"])
	print "\n"
	
	print "Listing running containers\n"
	call(["curl", "-s","-X GET","-H 'Accept:application/json'","localhost:8080/containers?state=running"])
	print "\n"

	print "Inspect a container\n"
	call(["curl", "-s","-X GET","-H 'Accept:application/json'","localhost:8080/containers/4a5bcb4508db"])
	print "\n"

	print "Deleting a container\n"
    call(["curl","-s","-X DELETE","-H 'Accept:application/json'","localhost:8080/containers/4a5bcb4508db"])
    print "\n"

	print "Delete all containers\n"
    call(["curl","-s","-X DELETE","-H 'Accept:application/json'","localhost:8080/containers"])
    print "\n"

	print "Creating a container from image\n"
    call(["curl","-s","-X POST","-H 'Accept:application/json'","localhost:8080/containers", "-d {\"image\":\"17b7d05c289\",\"publish\":\"8082:22\"}"])
    print "\n"

	print "Restarting a container\n"
    call(["curl","-s","-X PATCH","-H 'Accept:application/json'","localhost:8080/containers/15a877f30e90","-d {\"state\":\"running\"}"])
    print "\n"

	print "Stopping a container\n"
	call(["curl", "-s","-X PATCH","-H 'Accept:application/json'","localhost:8080/containers/ac816ef4ad19","-d {\"state\":\"stopped\"}"])
	print "\n"
	
	print "Showing container logs\n"
	call(["curl", "-s","-X GET","-H 'Accept:application/json'","localhost:8080/containers/15a877f30e90/logs"])
	print "\n"

	print "List all images\n"
	call(["curl", "-s","-X GET","-H 'Accept:application/json'","localhost:8080/images"])
	print "\n"

	print "Deleting an image\n"
	call(["curl", "-s","-X DELETE","-H 'Accept:application/json'","localhost:8080/images/e9ae3c220b23"])
	print "\n"

	print "Deleting all images\n"
	call(["curl", "-s","-X DELETE","-H 'Accept:application/json'","localhost:8080/images"])
	print "\n"

	print "Tagging an image\n"
	call(["curl", "-s","-X PATCH","-H 'Accept:application/json'","localhost:8080/images/17b7d05c289", "-d {\"tag\":\"test:1.0\"}"])
	print "\n"

	print "Creating docker image from dockerfile"
	call(["curl", "-s","-X POST","-H 'Accept:application/json'", "-F","file=@Dockerfile","localhost:8080/images"])
	print "\n"

if __name__ == '__main__':
	main()

