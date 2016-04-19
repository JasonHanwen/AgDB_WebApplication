<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Login.aspx.cs" Inherits="TestEmail.Login" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>   
            <p>Please INPUT YOUR EMAIL to verify</p>
            <asp:TextBox ID="Email" runat="server" />
    </div>
        <asp:Button ID="submit" runat="server" OnClick="submitButton_Click" Text="Submit" />
    </form>
</body>
</html>