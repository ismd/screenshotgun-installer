#
# Usage:
#
# make VERSION=<version> create-repo
# make VERSION=<version> update-repo
# make create-installer
#

create-repo:
	docker run --rm \
		-v .:/app \
		-v /srv/http:/srv/http \
		ismd/screenshotgun-installer \
		/app/scripts/create-repo.py \
		-c /app/config \
		-o /srv/http \
		-v $(VERSION)

update-repo:
	docker run --rm \
		-v .:/app \
		-v /srv/http:/srv/http \
		ismd/screenshotgun-installer \
		/app/scripts/update-repo.py \
		-c /app/config \
		-o /srv/http \
		-v $(VERSION)

create-installer:
	docker run --rm \
		-v .:/app \
		ismd/screenshotgun-installer \
		/app/scripts/create-installer.py \
		-o /app
