#
# Usage: make VERSION=<version> <target>
#

create_repo: update_packages
	./scripts/repo/create_repo.sh

update_repo: update_packages
	./scripts/repo/update_repo.sh

# Additional
update_packages:
	./scripts/update_packages.sh $(VERSION)
