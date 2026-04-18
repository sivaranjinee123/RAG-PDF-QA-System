// app/layout.tsx

// app/layout.tsx

import "./globals.css";
import { ReactNode } from "react";

export const metadata = {
  title: "RAG PDF QA System",
  description: "Upload PDF and ask questions",
};

export default function RootLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}