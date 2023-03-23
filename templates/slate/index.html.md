---
title: ${bblock.name} (${bblock.itemClass.capitalize()})
% if bblock.examples:
<%
  examples = {}
  non_lang_examples = []
  langs = set()
  for example in bblock.examples:
    lang = example.get('language')
    lang = None if lang in (None, '_', '') else lang
    langs.add(lang if lang else 'plaintext')
    if lang:
      examples.setdefault(example.get('title', 'Example'), []).append(example)
    else:
      non_lang_examples.append(example)
%>
language_tabs:
  % for lang in langs:
  - ${lang}
  % endfor
% endif

toc_footers:
  - Version ${bblock.version}
  - <a href="https://github.com/cportele/ogcapi-building-blocks#building-block-maturity">Maturity</a>: ${bblock.maturity.capitalize()}
  - <a href='#'>{bblock.name}</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: ${bblock.name} (${bblock.itemClass.capitalize()})
---

${'#'} Overview

${bblock.abstract}

% if bblock.description:
${'#'} Description

${bblock.description.replace('@@assets@@', assets_rel or '')}

% endif
% if bblock.examples:
${'#'} Examples

  % for title, title_examples in examples.items():
${'##'} ${title}
    % for example in title_examples:
      % if example.get('markdown'):
${example['content'].replace('@@assets@@', assets_rel or '')}
      % else:
```${example['language']}
${example['content']}
```
      % endif
    % endfor
  % endfor
  % for example in non_lang_examples:
    % if example.get('markdown'):
${example['content'].replace('@@assets@@', assets_rel or '')}
    % else:
```plaintext
${example['content']}
```
    % endif
  % endfor
% endif
% if bblock.schema:
${'#'} Schema

[schema.yaml](${bblock_rel}/schema.yaml)

```yaml
${bblock.schema_contents}
```
% endif
% if bblock.sources:
${'#'} Sources

  % for source in bblock.sources:
    % if source.get('link'):
* [${source['title']}](${source['link']})
    % else:
* ${source['title']}
    % endif
  % endfor
% endif