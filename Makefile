#
# Usage: make VERSION=<version> <target>
#

create_repo: update_packages
	./scripts/repo/create_repo.sh $(OUTPUT_PATH)

update_repo: update_packages
	./scripts/repo/update_repo.sh $(OUTPUT_PATH)

clean:
	rm -rf ./build

# Additional
update_packages:
	./scripts/update_packages.sh $(VERSION)
