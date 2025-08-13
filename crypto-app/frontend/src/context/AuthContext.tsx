import { createContext, useContext, useState, ReactNode } from 'react';
import axios from 'axios';

interface AuthContextType {
  token: string | null;
  login: (username: string, password: string) => Promise<void>;
  register: (username: string, password: string) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used within AuthProvider");
  return context;
};

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [token, setToken] = useState<string | null>(null);

  const login = async (username: string, password: string) => {
    const res = await axios.post('/api/auth/login/', { username, password });
    setToken(res.data.access);
    localStorage.setItem('token', res.data.access);
  };

  const register = async (username: string, password: string) => {
    await axios.post('/api/auth/register/', { username, password });
  };

  return (
    <AuthContext.Provider value={{ token, login, register }}>
      {children}
    </AuthContext.Provider>
  );
};