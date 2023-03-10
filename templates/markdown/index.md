# ${bblock.name} (${bblock.itemClass.capitalize()})

*Version ${bblock.version}*

${bblock.abstract}

% if bblock.maturity:
[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): ${bblock.maturity}
% endif

% if bblock.description:
${'##'} Description

${bblock.description.replace('@@assets@@', assets_rel or '')}

% endif
% if bblock.examples:
${'##'} Examples

  % for example in bblock.examples:
    <% has_language = example.get('language') not in (None, '', '_') %>
${'###'} ${example['title']}${f" ({example['language']})" if has_language else ''}

    % if example.get('markdown'):
${example['content'].replace('@@assets@@', assets_rel or '')}
    % else:
```${example['language'] if has_language else ''}
${example['content']}
```
    % endif

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