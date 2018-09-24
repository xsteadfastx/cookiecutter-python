.PHONY: all clean test cook_test cook_testing cook_rm_tempdir

TMPDIR := $(shell mktemp -d -u)

cook_test:
	$(MAKE) cook_testing || $(MAKE) cook_rm_tempdir


cook_testing:
	mkdir $(TMPDIR)
	cookiecutter --no-input -o $(TMPDIR) .
	cd $(TMPDIR)/my_python_project
	make -C $(TMPDIR)/my_python_project init
	make -C $(TMPDIR)/my_python_project test
	rm -rf $(TMPDIR)

cook_rm_tempdir:
	rm -rf $(TMPDIR)
	exit 1
