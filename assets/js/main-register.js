$(document).ready(function () {

  const getColor = (s) => {
    let hash = 0;
    for (let i = 0; i < s.length; i++) {
      hash = s.charCodeAt(i) + ((hash << 5) - hash);
    }
    let color = '#';
    for (let i = 0; i < 3; i++) {
      const value = (hash >> (i * 8)) & 0xFF;
      color += ('00' + value.toString(16)).substr(-2);
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
    $labelContainer.on('click', '.label-button', function(e) {
        e.preventDefault();
        const $this = $(this);
        if ($this.hasClass('active')) {
          $wrapper.find('.project').fadeIn();
          $labelContainer.removeClass('filtered');
          $this.removeClass('active');
        } else {
          const groupName = $this.data('group-name');
          $wrapper.find('.project')
            .filter((i, e) => $(e).data('group-name') !== groupName)
            .fadeOut(() => {
              groups[groupName].forEach($e => $e.fadeIn());
              $labelContainer.find('.active').removeClass('active');
              $this.addClass('active');
              $labelContainer.addClass('filtered');
            });
        }
      });

    $.get("./register.json")
      .then(bblocks => {
        bblocks.forEach(bblock => {
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

          const $labels = $('<div>')
            .addClass('label-container')
            .appendTo($block);

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

            //$block.css('box-shadow', '0 0 10px ' + groupColor);

            if (!groups[bblock.group]) {
              groups[bblock.group] = [];
            }
            groups[bblock.group].push($parent);
            $parent.data('group-name', bblock.group);
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

  function BadgePressed() {
    $("a#" + this.id).toggleClass("down");

    $('.project-label').each(function (index) {
      var projectId = this.getAttribute("for");
      var foundLabelStillActive = false;
      $('.project-label').each(function (index) {
        if (this.getAttribute("for") == projectId && !($(this).hasClass("down"))) {
          foundLabelStillActive = true;
        }
      });

      var hasClass = $("#" + projectId).hasClass("project-hidden");
      if (hasClass && foundLabelStillActive) {
        $("#" + projectId).removeClass("project-hidden");
      } else {
        if (!hasClass && !foundLabelStillActive) {
          $("#" + projectId).addClass("project-hidden");
        }
      }
    });
  }

  function AllBadgePressed() {
    $('.project-label').each(function (index) {
      if ($(this).hasClass("down")) {
        $(this).removeClass("down");
        var projectId = this.getAttribute("for");
        var hasClass = $("#" + projectId).hasClass("project-hidden");
        if (hasClass) {
          $("#" + projectId).removeClass("project-hidden");
        }
      }
    });
  }

  function NoneBadgePressed() {
    $('.project-label').each(function (index) {
      if (!$(this).hasClass("down")) {
        $(this).addClass("down");
        var projectId = this.getAttribute("for");
        var hasClass = $("#" + projectId).hasClass("project-hidden");
        if (!hasClass) {
          console.log("has class hidden");
          //console.log("#" + projectId);
          $("#" + projectId).addClass("project-hidden");
        }
      }
    });
  }

  function findLabel(labelId, newProject, badgeParent) {
    var label = '';
    var labelFound = false;
    for (k = 0; k < projectSettings.labels.length; k++) {
      if (projectSettings.labels[k].id == labelId) {
        labelFound = true;
        label = projectSettings.labels[k];
        break;
      }
    }
    if (labelFound) {
      var labelLink = document.createElement("a");
      var content = document.createTextNode(label.display_name);
      labelLink.appendChild(content);
      labelLink.id = "label-" + labelId;
      labelLink.setAttribute("for", newProject.itemIdentifier.replaceAll(".", "-")/*newProject.itemIdentifier*/);
      labelLink.classList.add("project-label");
      labelLink.classList.add("proj-label-" + labelId);
      $(labelLink).click(BadgePressed);
      badgeParent.appendChild(labelLink);
    }
  }

  function LoadProjectsFromJson(projectSettings) {

    // First build up the new CSS classes for badge button colours
    var newCss = "";
    for (i = 0; i < projectSettings.labels.length; i++) {
      var newLabel = projectSettings.labels[i];
      var includeWhite = "";
      if (newLabel.is_label_font_white) {
        includeWhite = "color: white !important;"
      }
      newCss = newCss + " .proj-label-" + newLabel.id + " { background-color: " + newLabel.hex_color + "; " + includeWhite + " }  .proj-label-" + newLabel.id + ":hover { background-color: " + newLabel.hex_hover_color + "; } ";
    }



    var style = document.createElement('style');
    if (style.styleSheet) {
      style.styleSheet.cssText = newCss;
    } else {
      style.appendChild(document.createTextNode(newCss));
      document.getElementsByTagName('head')[0].appendChild(style);
    }

    // Then add new badge buttons to top of page
    for (i = 0; i < projectSettings.labels.length; i++) {
      var newLabel = projectSettings.labels[i];
      var badge = document.createElement("a");
      var badgeText = document.createTextNode(newLabel.display_name);
      badge.appendChild(badgeText);
      badge.id = "label-" + newLabel.id;
      badge.classList.add("project-label");
      badge.classList.add("proj-label-" + newLabel.id);
      $(badge).click(BadgePressed);
      document.getElementById("label-container").appendChild(badge);
    }

    // Read blocks from register.json
    $.getJSON("./register.json", function (json) {
      console.log("Loaded BBlocks", json.length);
      // Then add projects
      for (i = 0; i < json.length; i++) {
        var newProject = json[i];
        // Create div containing project
        var bigParent = document.createElement("div");
        bigParent.classList.add("project");
        bigParent.classList.add("col-12");
        bigParent.classList.add("col-xl-6");
        //bigParent.id = newProject.itemIdentifier;
        bigParent.id = newProject.itemIdentifier.replaceAll(".", "-");

        var parent = document.createElement("div");
        parent.classList.add("project-block");
        bigParent.appendChild(parent);
        // Create a containing title
        var title = document.createElement("a");
        title.href = newProject.documentation.slate.url;
        title.setAttribute("target", "_blank");
        title.classList.add("project-title");
        var titleContent = document.createTextNode(newProject.name);
        title.appendChild(titleContent);
        parent.appendChild(title);
        // Create div containing links

        var linksParent = document.createElement("div");
        linksParent.classList.add("proj-small-link-parent");

        parent.appendChild(linksParent);
        // Create p containing description
        var description = document.createElement("a");
        description.classList.add("project-text");
        description.innerHTML = newProject.abstract;
        parent.appendChild(description);
        // Create div containing label badges
        var badgeParent = document.createElement("div");
        badgeParent.classList.add("label-container");
        for (j = 0; j < newProject.sources.length; j++) {
          var labelId = newProject.sources[j];
          //var label;
          //console.log(labelId);
          findLabel(labelId, newProject, badgeParent);
        }
        //console.log(newProject.status);
        findLabel(newProject.status, newProject, badgeParent);
        findLabel(newProject.maturity, newProject, badgeParent);
        findLabel(newProject.scope, newProject, badgeParent);
        parent.appendChild(badgeParent);
        // Add project to html
        document.getElementById("projects-parent").appendChild(bigParent);
      }
    });
  }

  /*$('.project-label').click(BadgePressed);
  $('#project-label-all').click(AllBadgePressed);
  $('#project-label-none').click(NoneBadgePressed);

  LoadProjectsFromJson(projectSettings);*/
  loadBBlocks();
});