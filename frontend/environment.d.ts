declare namespace NodeJS {
  interface ProcessEnv {
    NODE_ENV: "development" | "production" | "test";
    NEXT_PUBLIC_COLLAB_WS_URL: string;
    NEXT_PUBLIC_API_URL: string;
  }
}
