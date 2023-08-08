import { useState, useEffect } from 'react';
import socketIoClient from 'socket.io-client';

const ENDPOINT = 'serverUrl';

export default function OnlineUsers() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        const socket = socketIoClient(ENDPOINT);

        socket.on('count', (count) => {
            setCount(count);
        });

        window.addEventListener('beforeunload', () => {
            socket.emit('pageUnload');
        });

        return () => {
            socket.disconnect();
            window.removeEventListener('beforeunload', () => {
                socket.emit('pageUnload');
            });
        };
    }, []);
  
    return (
        <div>
            {count !== 0 && <div>Number of online users: {count}</div>}
        </div>
    )
}
