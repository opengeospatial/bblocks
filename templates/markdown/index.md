# ${bblock.name} (${bblock.itemClass.capitalize()})

*Version ${bblock.version}*

${bblock.abstract}

% if bblock.maturity:
[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): ${bblock.maturity.capitalize()}
% endif

% if bblock.description:
${'##'} Description

${bblock.description.replace('@@assets@@', assets_rel or '')}

% endif
% if bblock.examples:
${'##'} Examples

  % for example in bblock.examples:
${'###'} ${example.get('title', f"Example {loop.index + 1}")}

${example.get(content, '')}
    % for snippet in example.get('snippets', []):
${'####'} ${snippet['language']}
```${snippet['language']}
${snippet['code']}
```
    % endfor
  % endfor
% endif
% if bblock.schema:
${'##'} Schema

[schema.yaml](${bblock_rel}/schema.yaml)

```yaml
${bblock.schema_contents}
```
% endif
% if bblock.sources:
${'##'} Sources

  % for source in bblock.sources:
    % if source.get('link'):
* [${source['title']}](${source['link']})
    % else:
* ${source['title']}
    % endif
  % endfor
% endif