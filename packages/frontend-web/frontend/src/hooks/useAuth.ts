import { useMemo, useState } from "react";

const TOKEN_KEY = "blender-frontend-web-api-token";
const THEME_KEY = "blender-frontend-web-theme";

export type ThemeMode = "dark" | "light";

function readStorage(key: string): string {
  const value = window.localStorage.getItem(key);
  return value ?? "";
}

export function useAuth() {
  const [apiToken, setApiTokenState] = useState<string>(readStorage(TOKEN_KEY));
  const [theme, setThemeState] = useState<ThemeMode>(() => {
    const stored = readStorage(THEME_KEY);
    return stored === "light" ? "light" : "dark";
  });

  const isAuthenticated = useMemo(() => apiToken.length > 0, [apiToken]);

  function setApiToken(nextToken: string) {
    setApiTokenState(nextToken);
    window.localStorage.setItem(TOKEN_KEY, nextToken);
  }

  function clearApiToken() {
    setApiTokenState("");
    window.localStorage.removeItem(TOKEN_KEY);
  }

  function setTheme(nextTheme: ThemeMode) {
    setThemeState(nextTheme);
    window.localStorage.setItem(THEME_KEY, nextTheme);
  }

  return {
    apiToken,
    isAuthenticated,
    setApiToken,
    clearApiToken,
    theme,
    setTheme
  };
}
