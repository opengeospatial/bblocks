#!/usr/bin/env python3

import json
from os.path import relpath
from pathlib import Path
from argparse import ArgumentParser
from typing import Sequence
from urllib.parse import urljoin

from mako.template import Template as MakoTemplate
from mako.lookup import TemplateLookup
from mako import exceptions

from scripts.util import load_bblocks, BuildingBlock


class DocTemplate:

    def __init__(self, p: Path):
        self.path = p
        self.ext = p.suffix
        self.lang = p.parent.name
        self.filename = p.name

        self._lookup = TemplateLookup(directories=[p.parent])
        self._template = MakoTemplate(filename=str(p), lookup=self._lookup)

    def render(self, **kwargs) -> str:
        try:
            return self._template.render(**kwargs)
        except:
            print(exceptions.text_error_template().render())
            raise


def find_templates(root: Path) -> list[DocTemplate]:
    return [DocTemplate(p) for p in root.glob('*/*') if not p.name.startswith("_")]


class DocGenerator:

    def __init__(self, output_dir: str | Path = 'generateddocs'):
        self.output_dir = output_dir if isinstance(output_dir, Path) else Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.templates = find_templates(Path('templates'))
        for template in self.templates:
            self.output_dir.joinpath(template.lang).mkdir(parents=True, exist_ok=True)

    def generate_doc(self, bblock: BuildingBlock, base_url: str = None):
        for template in self.templates:
            tpl_out = self.output_dir / template.lang / bblock.subdirs / template.filename
            tpl_out.parent.mkdir(parents=True, exist_ok=True)
            bblock_rel = relpath(bblock.files_path, tpl_out.parent)
            assets_rel = relpath(bblock.assets_path, tpl_out.parent) if bblock.assets_path else None
            if base_url:
                tpl_out_url = urljoin(base_url, relpath(tpl_out))
                bblock_rel = urljoin(tpl_out_url, bblock_rel)
                if assets_rel:
                    assets_rel = urljoin(tpl_out_url, assets_rel)
            with open(tpl_out, 'w') as f:
                f.write(template.render(bblock=bblock,
                                        bblock_rel=bblock_rel,
                                        tplfile=template.path,
                                        outfile=tpl_out,
                                        assets_rel=assets_rel,
                                        root_dir=Path(),
                                        base_url=base_url))
                if base_url and template.path.stem == 'index':
                    doc_url = f"{base_url}{'/' if base_url[-1] not in ('/', '#') else ''}" \
                              f"{self.output_dir.name}/{template.lang}/{bblock.subdirs}/{template.filename}"
                    existing = bblock.metadata.setdefault('documentation', [])
                    if doc_url not in existing:
                        existing.append(doc_url)


def generate_docs(regs: str | Path | Sequence[str | Path],
                  filter_ids: str | list[str] | None = None,
                  output_dir: str | Path = 'generateddocs'):
    doc_generator = DocGenerator(output_dir)

    def do_postprocess(bblock: BuildingBlock):
        doc_generator.generate_doc(bblock)

    load_bblocks(regs, filter_ids, do_postprocess)


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
