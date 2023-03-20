from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence

from scripts.generate_docs import DocGenerator
from scripts.util import load_bblocks, BuildingBlock


def postprocess(regs: str | Path | Sequence[str | Path],
                filter_ids: str | list[str] | None = None,
                base_url: str | None = None):
    doc_generator = DocGenerator()

    if base_url and base_url[-1] not in ('/', '#'):
        base_url += '/'

    def do_postprocess(bblock: BuildingBlock):
        cwd = Path()
        if base_url:
            if bblock.schema:
                rel_schema = bblock.schema.relative_to(cwd)
                schema_url = f"{base_url}{rel_schema}"
                existing_schemas = bblock.metadata.setdefault('schema', [])

                if bblock.annotated_schema:
                    rel_annotated = bblock.annotated_schema.relative_to(cwd)
                    add_schema_url = f"{base_url}{rel_annotated}"

                    # Remove old, non-annotated schema if present
                    if schema_url in existing_schemas:
                        existing_schemas.remove(schema_url)
                else:
                    add_schema_url = schema_url

                if add_schema_url not in existing_schemas:
                    existing_schemas.append(add_schema_url)

        doc_generator.generate_doc(bblock, base_url=base_url)

    load_bblocks(regs, filter_ids, do_postprocess)


def _main():
    parser = ArgumentParser()

    parser.add_argument(
        'register_doc',
        nargs='+',
        help='JSON Building Blocks register document(s)',
    )

    parser.add_argument(
        '-u',
        '--base-url',
        help='Base URL for hyperlink generation',
    )

    parser.add_argument(
        '-i',
        '--filter-id',
        nargs='+',
        help='Only process building blocks matching these ids',
    )

    args = parser.parse_args()

    postprocess(args.register_doc,
                filter_ids=args.filter_id,
                base_url=args.base_url)


if __name__ == '__main__':
    _main()
