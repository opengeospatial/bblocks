import json
from pathlib import Path
from typing import Callable, Sequence

import yaml

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
        self.subdirs = Path(*self.identifier.split('.')[1:])
        fp = Path('registereditems') / self.subdirs
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

        annotated_path = Path('annotated') / self.subdirs
        if annotated_path.is_dir():
            self.annotated_path = annotated_path
            annotated_schema = annotated_path / 'schema.yaml'
            self.annotated_schema = annotated_schema if annotated_schema.exists() else None
            jsonld_context = annotated_path / 'context.jsonld'
            self.jsonld_context = jsonld_context if jsonld_context.exists() else None
        else:
            self.annotated_path = None
            self.annotated_schema = None
            self.jsonld_context = None

    def __getattr__(self, item):
        return self.metadata.get(item)


def load_bblocks(regs: str | Path | Sequence[str | Path],
                 filter_ids: str | list[str] | None = None,
                 callback: Callable[[BuildingBlock], None] = None):
    if not callback:
        return

    if not isinstance(regs, Sequence) or isinstance(regs, str):
        regs = [regs]
    if isinstance(filter_ids, str):
        filter_ids = [filter_ids]

    for reg in regs:
        updated_metadata = []
        if not isinstance(reg, Path):
            reg = Path(reg)
        with open(reg) as f:
            bblocks = json.load(f)
        for bblock_metadata in bblocks:
            if filter_ids and not bblock_metadata['itemIdentifier'] in filter_ids:
                continue
            bblock = BuildingBlock(bblock_metadata)
            callback(bblock)
            updated_metadata.append(bblock.metadata)

        with open(reg, 'w') as f:
            json.dump(updated_metadata, f, indent=2)
