import { paths } from "@/types/api-schema";
import createFetchClient, { Middleware } from "openapi-fetch";
import createClient from "openapi-react-query";

const fetchClient = createFetchClient<paths>({
  baseUrl: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8080",
});

const authMiddleWare: Middleware = {
  async onRequest({ request, options }) {
    const token = document.cookie
      .split("; ")
      .find((row) => row.startsWith("access_token="))
      ?.split("=")[1];
    if (!token) {
      console.error("No access token found in cookies");
    }
    if (token) {
      request.headers.set("Authorization", `Bearer ${token}`);
      console.log("Token found in cookies");
    }

    return request;
  },
};

fetchClient.use(authMiddleWare);
export const apiClient = createClient(fetchClient);
