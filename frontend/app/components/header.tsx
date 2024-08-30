import Image from "next/image";

export default function Header() {
  return (
    <div className="z-10 max-w-5xl mx-auto flex flex-col items-center justify-center font-mono text-sm py-4">
      <div className="flex flex-col items-center justify-center w-full">
        <Image
          className="rounded-xl mb-4"
          src="/lds-logo.png"
          alt="lds Logo"
          width={150}
          height={150}
          priority
        />
        <h1 className="text-white text-center text-[1rem] md:text-[2.5rem] lg:text-[3.5rem] leading-none font-TenorSans">
          LDS Handbook Chatbot
        </h1>
      </div>
    </div>
  );
}
