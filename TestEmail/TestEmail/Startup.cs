using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(TestEmail.Startup))]
namespace TestEmail
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}
