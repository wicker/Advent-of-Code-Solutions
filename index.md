---
layout: page
special: true
header: mccall.png
---

Hi! These are solutions in Python for <a href="http://adventofcode.com/">the Advent of Code</a>, which was a set of programming puzzles released one per day in December 2015. You can find my other code and projects elsewhere on <a  href="http://jennerhanni.net">my website</a> or at my <a href="http://github.com/wicker/">github account</a>.

<ol style="margin: 0px; padding: 0px; list-style-type: decimal">
{% for post in site.posts reversed %}
<li><a href="http://jennerhanni.net/advent-of-code/{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ol>
