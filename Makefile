# Variables
SCRIPT_NAME = extract_audio.py
VERSION = 1.0.1
TAR_FILE = v$(VERSION).tar.gz
GITHUB_USER = cajias
REPO_NAME = v2a

.PHONY: all release clean

all: release

# Create a tarball of the script
$(TAR_FILE): $(SCRIPT_NAME)
	tar -czvf $(TAR_FILE) $(SCRIPT_NAME)

# Create a GitHub release and upload the tarball
release: $(TAR_FILE)
	# Create GitHub release
	gh release create v$(VERSION) $(TAR_FILE) --title "v$(VERSION)" --notes "Release version $(VERSION)"
	curl -L -o $(TAR_FILE) https://github.com/$(GITHUB_USER)/$(REPO_NAME)/archive/refs/tags/$(TAR_FILE)
	# Get the SHA-256 checksum of the tarball
	@shasum -a 256 $(TAR_FILE) | tr -s ' ' | cut -d ' ' -f 1

# delete release from github
undo-release:
	gh release delete v$(VERSION)
	# delete tag
	git tag -d v$(VERSION)


clean:
	rm -f $(TAR_FILE)
