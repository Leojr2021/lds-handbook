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
        <h1 className="text-center text-[2rem] md:text-[3rem] lg:text-[4.375rem] leading-none">
          LDS Handbook Chatbot
        </h1>
      </div>
    </div>
  );
}
