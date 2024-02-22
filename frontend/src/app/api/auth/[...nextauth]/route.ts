import NextAuth from "next-auth";
import GoogleProvider from "next-auth/providers/google";

const handler = NextAuth({
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID ?? "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET ?? "",
    }),
  ],
  callbacks: {
    async signIn({ user, account, profile }) {
      const allowedEmail = 'adrenaline2142@gmail.com';
      if (user.email === allowedEmail) {
        return true;
      } else {
        return false;
      }
    },
  },
})


export { handler as GET, handler as POST };
