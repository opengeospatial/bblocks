import json
from pathlib import Path
import os.path
from typing import Callable, Sequence, Generator, Any
import jsonschema
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


def get_bblock_identifier(metadata_file: Path, root_path: Path = Path()) -> tuple[str, Path]:
    rel_parts = Path(os.path.relpath(metadata_file.parent, root_path)).parts[1:]
    return 'r1.' + '.'.join(rel_parts), Path(*rel_parts)


class BuildingBlock:

    def __init__(self, identifier: str, metadata_file: Path,
                 rel_path: Path,
                 metadata_schema: Any | None = None,
                 root_path: Path = Path()):
        self.identifier = identifier
        with open(metadata_file) as f:
            self.metadata = json.load(f)

            if metadata_schema:
                jsonschema.validate(self.metadata, metadata_schema)

            self.metadata['itemIdentifier'] = identifier

        self.subdirs = rel_path

        fp = metadata_file.parent
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

        annotated_path = root_path / 'annotated' / self.subdirs
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


def load_bblocks(registered_items_path: Path,
                 root_path: Path = Path(),
                 filter_ids: str | list[str] | None = None,
                 metadata_schema_file: str | Path | None = None) -> Generator[BuildingBlock, None, None]:

    if metadata_schema_file:
        metadata_schema = load_yaml(metadata_schema_file)
    else:
        metadata_schema = None

    for metadata_file in sorted(registered_items_path.glob("**/metadata.json")):
        bblock_id, bblock_rel_path = get_bblock_identifier(metadata_file, root_path)
        if not filter_ids or bblock_id in filter_ids:
            yield BuildingBlock(bblock_id, metadata_file,
                                metadata_schema=metadata_schema,
                                rel_path=bblock_rel_path,
                                root_path=root_path)
