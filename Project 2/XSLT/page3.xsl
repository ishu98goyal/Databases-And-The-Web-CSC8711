<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template name="details">
  <xsl:param name="e"/>
    <style>
  table {
    width: 80%;
    margin: auto;
    border-collapse: collapse;
  }

  th, td {
    border: 1px solid black;
    padding: 10px;
    text-align: left;
  }

  th {
    background-color: lightgray;
  }

  ul {
    margin: 0;
    padding: 0;
    list-style-type: none;

  }
</style>

<table>
  <tr>
    <th>Title</th>
    <td>
    <xsl:value-of select="concat(translate(substring(title, 1, 1), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), substring(title, 2))"/>
    </td>
  </tr>
  <tr>
    <th>Year</th>
    <td><xsl:value-of select="year"/></td>
  </tr>
  <tr>
    <th>Director(s)</th>
    <td>
      <xsl:for-each select="directors/director">
        <xsl:variable name="idref" select="@idref"/>
        <xsl:value-of select="//performers/performer[@id=$idref]/name"/>
        <xsl:if test="following-sibling::*">, </xsl:if>
      </xsl:for-each>
    </td>
  </tr>
  <tr>
    <th>Genres</th>
    <td>
      <xsl:for-each select="genres/genre">
        <xsl:value-of select="text()"/>
        <xsl:if test="following-sibling::*">, </xsl:if>
      </xsl:for-each>
    </td>
  </tr>
  <tr>
    <th>Plot</th>
    <td><xsl:value-of select="plot"/></td>
  </tr>
  <tr>
    <th>Cast</th>
    <td>
      <xsl:for-each select="cast/performer">
        <ul>
          <xsl:variable name="actor" select="actor/@idref"/>
          <li><b>Actor: </b><xsl:value-of select="//performers/performer[@id=$actor]/name"/></li><li><b>Role: </b><xsl:value-of select="role"/></li>
          <br></br>
        </ul>
        <xsl:if test="following-sibling::*"></xsl:if>
      </xsl:for-each>
    </td>
  </tr>
</table>

</xsl:template>

<xsl:template match="/">
  <xsl:for-each select="mdb/movies/movie">
    <xsl:if test="title=$name">
      <xsl:call-template name="details">
      <xsl:param name="e"> 
        <xsl:value-of select="title"/>
        
      </xsl:param> 
    </xsl:call-template>
    </xsl:if>
  </xsl:for-each>
</xsl:template>


</xsl:stylesheet>
