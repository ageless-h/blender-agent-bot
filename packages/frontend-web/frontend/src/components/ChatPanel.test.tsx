import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

import { ChatPanel } from "./ChatPanel";

describe("ChatPanel", () => {
  test("渲染消息并触发发送", async () => {
    const user = userEvent.setup();
    const onSend = vi.fn(async () => {});

    render(
      <ChatPanel
        messages={[
          {
            id: "1",
            role: "assistant",
            user: "assistant",
            message: "hello",
            created_at: new Date().toISOString(),
          },
        ]}
        streamingText=""
        isSending={false}
        connectionText="已连接"
        onSend={onSend}
      />
    );

    expect(screen.getByText("hello")).toBeInTheDocument();

    await user.type(screen.getByPlaceholderText("输入对 Blender 的指令..."), "创建立方体");
    await user.click(screen.getByRole("button", { name: "发送" }));

    expect(onSend).toHaveBeenCalledWith("创建立方体");
  });
});
