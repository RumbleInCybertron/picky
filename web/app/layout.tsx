export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className="bg-gray-100 min-h-screen flex items-center justify-center"
      >
        {children}
      </body>
    </html>
  );
}
