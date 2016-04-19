<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="FirstWebPage.aspx.cs" Inherits="TestEmail.FirstWebPage" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
            hello world<br />
            <br />
            Enter your Name<br />
            <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button1" runat="server" Text="Button" />
            <br />
            <br />
            <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </div>
    </form>
</body>
</html>
