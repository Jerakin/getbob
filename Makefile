clean:
	rm -rf *.egg-info
	rm -rf dist

build:
	python setup.py bdist_wheel

install:
	pip install ./dist/getbob-$(shell cat "./getbob/__init__.py" | grep -Eo -m 1 "[0-9\.ab]{5,}")-py3-none-any.whl

publish:
	python setup.py bdist_wheel
	twine upload ./dist/getbob-$(shell cat "./getbob/__init__.py" | grep -Eo "[0-9\.ab]{5,}")-py3-none-any.whl
	git tag v$(shell cat "./getbob/__init__.py" | grep -Eo "[0-9\.ab]{5,}")

.PHONY: clean build install publish

