<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template name="MovieTemplate">
  <xsl:param name="name"/>
  <a href="#" onclick="displayDetails('{$name}');"><xsl:value-of select="title"/> (<xsl:value-of select="year"/>)</a>
  <hr></hr>
  <br></br>
</xsl:template>

<xsl:template match="/mdb">
  <xsl:for-each select="movies/movie">
    <xsl:variable name="s" select="'abcdefghijklmnopqrstuvwxyz'" />
    <xsl:variable name="u" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
    <xsl:if test="starts-with(translate(substring(title, 1, 1), $s, $u), $m)">
      <xsl:call-template name="MovieTemplate">
        <xsl:with-param name="name"> 
          <xsl:value-of select="title"/>
        </xsl:with-param> 
      </xsl:call-template>
    </xsl:if>
  </xsl:for-each>
</xsl:template>

</xsl:stylesheet>
