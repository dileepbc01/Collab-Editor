import { paths } from "@/types/api-schema";
import createFetchClient from "openapi-fetch";
import createClient from "openapi-react-query";

const fetchClient = createFetchClient<paths>({
  baseUrl: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8080",
});

export const apiClient = createClient(fetchClient);
