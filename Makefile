# Variables
SCRIPT_NAME = convert_to_mp3.py
VERSION = 1.0.0
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
	# Get the SHA-256 checksum of the tarball
	SHA256=$$(shasum -a 256 $(TAR_FILE) | awk '{ print $$1 }')
	# Print SHA-256 checksum
	@echo "SHA-256 checksum: $$SHA256"

clean:
	rm -f $(TAR_FILE)