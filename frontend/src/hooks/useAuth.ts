import { apiClient } from "@/lib/api";

export const useAuth = () => {
  const { data, error, isLoading } = apiClient.useQuery("get", "/auth/me", {
    queryKey: ["auth", "me"],
  });

  return {
    user: data,
    error,
    isLoading,
  };
};
