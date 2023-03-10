#!/usr/bin/env python3

import json
from os.path import relpath
from pathlib import Path
from argparse import ArgumentParser
from typing import Sequence
import yaml
from mako.template import Template as MakoTemplate
from mako.lookup import TemplateLookup

try:
    from yaml import CLoader as YamlLoader
except ImportError:
    from yaml import Loader as YamlLoader


def load_yaml(fn):
    with open(fn) as f:
        return yaml.load(f, Loader=YamlLoader)


def load_file(fn):
    with open(fn) as f:
        return f.read()


class BuildingBlock:

    def __init__(self, metadata: dict):
        self.identifier = metadata['itemIdentifier']
        self.metadata = metadata
        fp = Path('registereditems').joinpath(*self.identifier.split('.')[1:])
        self.files_path = fp

        examples_file = fp / 'examples.yaml'
        self.examples = load_yaml(examples_file) if examples_file.exists() else None

        desc_file = fp / 'description.md'
        if desc_file.exists():
            self.description = load_file(desc_file)
        else:
            self.description = None

        ap = fp / 'assets'
        self.assets_path = ap if ap.is_dir() else None

        schema = fp / 'schema.yaml'
        if schema.is_file():
            self.schema = schema
            self.schema_contents = load_file(schema)
        else:
            self.schema = None
            self.schema_contents = None

    def __getattr__(self, item):
        return self.metadata.get(item)


class DocTemplate:

    def __init__(self, p: Path):
        self.path = p
        self.ext = p.suffix
        self.lang = p.parent.name
        self.filename = p.name

        self._lookup = TemplateLookup(directories=[p.parent])
        self._template = MakoTemplate(filename=str(p), lookup=self._lookup)

    def render(self, **kwargs) -> str:
        return self._template.render(**kwargs)


def find_templates(root: Path) -> list[DocTemplate]:
    return [DocTemplate(p) for p in root.glob('*/*') if not p.name.startswith("_")]


def generate_docs(regs: str | Path | Sequence[str | Path],
                  filter_ids: str | list[str] | None = None,
                  output_dir: str | Path = 'generateddocs'):
    if not isinstance(regs, Sequence) or isinstance(regs, str):
        regs = [regs]
    if isinstance(filter_ids, str):
        filter_ids = [filter_ids]
    if not isinstance(output_dir, Path):
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    templates = find_templates(Path('templates'))
    for template in templates:
        output_dir.joinpath(template.lang).mkdir(parents=True, exist_ok=True)

    for reg in regs:
        if not isinstance(reg, Path):
            reg = Path(reg)
        with open(reg) as f:
            bblocks = json.load(f)
        for bblock_metadata in bblocks:
            if filter_ids and not bblock_metadata['itemIdentifier'] in filter_ids:
                continue
            bblock = BuildingBlock(bblock_metadata)
            for template in templates:
                tpl_out = output_dir / template.lang / bblock.identifier / template.filename
                tpl_out.parent.mkdir(parents=True, exist_ok=True)
                bblock_rel = relpath(bblock.files_path, tpl_out.parent)
                assets_rel = relpath(bblock.assets_path, tpl_out.parent) if bblock.assets_path else None
                with open(tpl_out, 'w') as f:
                    f.write(template.render(bblock=bblock,
                                            bblock_rel=bblock_rel,
                                            tplfile=template.path,
                                            outfile=tpl_out,
                                            assets_rel=assets_rel))


def _main():
    parser = ArgumentParser()

    parser.add_argument(
        'register_doc',
        nargs='+',
        help='JSON Building Blocks register document(s)',
    )

    parser.add_argument(
        '-i',
        '--filter-id',
        nargs='+',
        help='Only process building blocks matching these ids',
    )

    parser.add_argument(
        '-o',
        '--output-dir',
        help='Output directory',
        default='generateddocs'
    )

    args = parser.parse_args()

    generate_docs(args.register_doc, filter_ids=args.filter_id, output_dir=args.output_dir)


if __name__ == '__main__':
    _main()
