$(document).ready(function () {

  const validStatuses = [
    'valid',
    'experimental',
    'stable',
  ];

  const getColor = (s) => {
    let hash = 0;
    for (let i = 0; i < s.length; i++) {
      hash = s.charCodeAt(i) + ((hash << 5) - hash);
    }
    let color = '#';
    for (let i = 0; i < 3; i++) {
      const value = (hash >> (i * 8)) & 0xFF;
      const x = '00' + value.toString(16)
      color += x.substring(x.length - 2);
    }
    return color;
  };

  const useWhiteText = (color) => {
    const colorNum = parseInt(color.substring(1), 16);
    const red = (colorNum >> 16);
    const blue = ((colorNum >> 8) & 0x00FF);
    const green = (colorNum & 0x0000FF);
    return (red * 0.299 + green * 0.587 + blue * 0.114) <= 186;
  };

  const loadBBlocks = () => {
    const $wrapper = $('#projects-parent');
    const groups = {};
    const $labelContainer = $('#label-container');
    const $hideInvalid = $('input#hide-invalid');

    const updateFilters = () => {
      const groupName = $labelContainer.find('.active').data('group-name');
      const hideInvalid = $hideInvalid.is(':checked');
      const $projects = $wrapper.find('.project').stop();
      if (!groupName && !hideInvalid) {
        // Show all
        console.log('show all')
        $projects.fadeIn();
      } else {
        const $projectsOn = $projects
          .filter((i, e) => (!groupName || $(e).data('group-name') === groupName)
                          && (!hideInvalid || $(e).data('bblock-valid')));
        console.log("on:", $projectsOn)
        $projects.not($projectsOn).fadeOut(() => $projectsOn.fadeIn());
      }
    };

    $labelContainer.on('click', '.label-button', function (e) {
      e.preventDefault();
      const $this = $(this);
      if ($this.hasClass('active')) {
        $wrapper.find('.project').fadeIn();
        $labelContainer.removeClass('filtered');
        $this.removeClass('active');
      } else {
        $labelContainer.find('.active').removeClass('active');
        $this.addClass('active');
        $labelContainer.addClass('filtered');
      }
      updateFilters();
    });
    $hideInvalid.change(updateFilters);

    $.get("./register.json")
      .then(bblocks => {
        bblocks.sort((a, b) => a.itemIdentifier.localeCompare(b.itemIdentifier)).forEach(bblock => {
          const docLink = bblock.documentation.slate.url;

          const $parent = $('<div>')
            .attr('id', bblock.itemIdentifier.replaceAll('.', '-'))
            .addClass('project col-12 col-xl-6')
            .appendTo($wrapper);

          const $block = $('<div>').addClass('project-block')
            .appendTo($parent);

          const $title = $('<div>')
            .addClass('project-title')
            .appendTo($block);
          $('<a>')
            .attr({
              href: docLink,
              target: '_blank',
            })
            .text(bblock.name)
            .appendTo($title);
          $('<small>')
            .addClass('version')
            .text('v' + bblock.version)
            .appendTo($title);

          $('<p>')
            .addClass('project-text')
            .text(bblock.abstract)
            .appendTo($block);

          const $projectBottom = $('<div>')
            .addClass('project-bottom')
            .appendTo($block);
          const $labels = $('<div>')
            .addClass('label-container')
            .appendTo($projectBottom);
          if (bblock.group) {
            const groupColor = getColor(bblock.group);
            $('<span>')
              .addClass('group-name project-label')
              .css({
                background: groupColor,
                color: useWhiteText(groupColor) ? 'white' : null,
              })
              .text(bblock.group)
              .appendTo($labels);

            if (!groups[bblock.group]) {
              groups[bblock.group] = [];
            }
            groups[bblock.group].push($parent);
            $parent.data('group-name', bblock.group);
          }
          const valid = validStatuses.includes(bblock.status);
          $('<a>')
            .addClass('status')
            .addClass(valid ? 'valid' : 'invalid')
            .attr({
              target: '_blank',
              href: `http://www.opengis.net/def/status/${bblock.status}`
            })
            .text(bblock.status.charAt(0).toUpperCase() + bblock.status.substring(1))
            .appendTo($projectBottom);
          $parent.data('bblock-valid', valid);
          if (!valid) {
            $parent.css('display', 'none');
          }
        });

        Object.keys(groups).forEach(group => {
          $('<a>')
            .addClass('label-button project-label')
            .css({
              background: getColor(group),
              color: useWhiteText(group) ? 'white' : null,
            })
            .text(group)
            .attr('href', '#')
            .data('group-name', group)
            .appendTo($labelContainer);
        });
      });
  };

  loadBBlocks();
});