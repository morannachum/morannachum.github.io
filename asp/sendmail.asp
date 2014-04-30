' Modified from the ASP posted to http://www.csudh.edu/webmaster/asp/
' Thank you, higher education!

<%
Dim mail, body

body = "Sender: " & Request.Form("name") & vbcrlf & "Sender E-mail: " & Request.Form("email") & vbcrlf & vbcrlf & "Message: " & vbcrlf & Request.Form("message")

Set mail = Server.CreateObject("CDO.Message")
mail.To = Request.Form("to")
mail.From = Request.Form("email")
mail.Subject = Request.Form("subject")
mail.TextBody = body
mail.Send()

Response.Write("Thank you for getting in touch!  I'll respond to your message as soon as I can.")

Set mail = nothing
Set body = nothing
%>