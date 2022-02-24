<h1 align="center">kilroyshare</h1>

---

This `README` provides info about the development process.

For more info about the package itself see `kilroyshare/README.md`.

## Continuous Integration

When you push changes to remote, different GitHub Actions run to ensure project
consistency. There are defined workflows for:

- drafting release notes
- uploading releases to PyPI

For more info see the files in `.github/workflows` directory and `Actions` tab
on GitHub.

## Releases

Every time you merge a pull request into main, a draft release is automatically
updated, adding the pull request to changelog. Changes can be categorized by
using labels. You can configure that in `.github/release-drafter.yml` file.

Every time you publish a release, the package is uploaded to PyPI with version
taken from release tag (ignoring the version in source code). You should store
your PyPI token in `PYPI_TOKEN` secret.
