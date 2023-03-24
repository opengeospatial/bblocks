---
title: ${bblock.name} (${bblock.itemClass.capitalize()})
% if bblock.examples:
<%
  langs = set(snippet['language'] for example in bblock.examples for snippet in example.get('snippets', []))
%>
language_tabs:
  % for lang in langs:
  - ${lang}
  % endfor
% endif

toc_footers:
  - Version ${bblock.version}
  - <a href='#'>${bblock.name}</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: ${bblock.name} (${bblock.itemClass.capitalize()})
---

${'#'} Overview

${bblock.abstract}

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): ${bblock.maturity.capitalize()}

% if bblock.description:
${'#'} Description

${bblock.description.replace('@@assets@@', assets_rel or '')}
% endif
% if bblock.examples:
${'#'} Examples
  % for example in bblock.examples:

${'##'} ${example.get('title', f"Example {loop.index + 1}")}

    % if example.get('content'):
${example['content'].replace('@@assets@@', assets_rel or '')}
    %endif
    % for snippet in example.get('snippets', []):
```${snippet['language']}
${snippet['code']}
```

    % endfor
  % endfor
% endif
% if bblock.schema:
${'#'} Schema

[schema.yaml](${bblock_rel}/schema.yaml)
###
### ```yaml
###${bblock.schema_contents}
### ```
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
