#
# Usage:
#
# make VERSION=<version> OWNER=<user> GROUP=<group> OUTPUT=<dir> create-repo
# make VERSION=<version> OWNER=<user> GROUP=<group> OUTPUT=<dir> update-repo
# make VERSION=<version> TYPE=<macos|windows> OUTPUT=<filename> create-installer
#

create-repo:
	docker run --rm \
		-v ${PWD}:/app \
		-v $(OUTPUT):/output \
		ismd/screenshotgun-installer \
		/app/src/create-repo.py \
		-c /app/config \
		-o /output \
		-v $(VERSION)
	sudo chown -R $(OWNER):$(GROUP) $(OUTPUT)

update-repo:
	docker run --rm \
		-v ${PWD}:/app \
		-v $(OUTPUT):/output \
		ismd/screenshotgun-installer \
		/app/src/update-repo.py \
		-c /app/config \
		-o /output \
		-v $(VERSION)
	sudo chown -R $(OWNER):$(GROUP) $(OUTPUT)

create-installer:
	docker run --rm \
		-v ${PWD}:/app \
		ismd/screenshotgun-installer \
		/app/src/create-installer.py \
		-o /app/$(OUTPUT) \
		-v $(VERSION) \
		-t $(TYPE)
