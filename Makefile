.PHONY: all clean test cook_test cook_testing cook_rm_tempdir

TMPDIR := $(shell mktemp -d -u)

cook_test:
	$(MAKE) cook_testing || $(MAKE) cook_rm_tempdir


cook_testing:
	mkdir $(TMPDIR)
	cookiecutter --no-input -o $(TMPDIR) .
	make -C $(TMPDIR)/my_python_project init
	make -C $(TMPDIR)/my_python_project test
	make -C $(TMPDIR)/my_python_project docs
	rm -rf $(TMPDIR)

cook_rm_tempdir:
	rm -rf $(TMPDIR)
	exit 1
