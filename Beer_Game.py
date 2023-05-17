import pandas as pd
import numpy as np
import random 

class Table:
    def __init__(self):
        self.Inventory=0#현재재고
        self.incoming_delivery=0#도착한 물건
        self.available=0#판매 가능량
        self.backorder=0#배송 미달량
        self.total_order=0#전체 배송 요청
        self.delivery=0#배송량
        self.incoming_order= 0#요청된 배송
        self.cost=0#현재 지출 비용
        self.order=0#발주량
        self.on_delivery=0#나에게 배송중인양
        
    def Incoming_delivery(self,deliver):
        self.incoming_delivery=deliver
        
    def inventory(self,past_inventory):
        self.Inventory=past_inventory
        
    def Available_update(self):#현재 판매 가능량 업데이트
        self.available=self.incoming_delivery+self.Inventory
        
    def Incoming_order(self,order):
        self.incoming_order=order
        
    def Backorder(self,past_backorder):#부족한 재고
        self.backorder=past_backorder

    def Total_order(self):#총 주문량
        self.total_order= self.backorder+self.incoming_order

    def Delivery(self):#총 배송량
        self.delivery= min(self.available,self.total_order)
        self.backorder=abs(min(self.available-self.incoming_order,0))
        
    def Cost(self,cost):
        if self.backorder>0:
            
            self.cost=self.cost-(2)*self.backorder

        else:
            self.cost=self.cost-self.Inventory
            
    def Order(self):#발주 입력  
        print("정규 발주")  
        self.order=int(input())
        
    def On_delivery(self,on_delivery):
        self.on_delivery=on_delivery
    
             
def Retailer_Env(x,Retailer,Retailer_df,Present_inventory,Wholesaler_df):

    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        first_inventory=random.randint(0, 10)
        Retailer.Inventory=(first_inventory)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        #Inventory 업데이트
        
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
    
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        print("Present Inventory",Present_inventory)
        #발주 해야하는 양
        Retailer.Order()
        
        
        
    
    elif x==1:
        Retailer.Incoming_delivery(0)
        
        Retailer.inventory=Present_inventory
        Retailer.Available_update()
        
        Retailer.Incoming_order(abs(round(np.random.randn(1)[0]*10)))
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(0)
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        print("Present Cost:",-1*Retailer.cost,"Present Inventory:",Present_inventory)
        #발주 해야하는 양
        Retailer.Order()
        
        
    elif x==2:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(abs(round(np.random.randn(1)[0]*10)))
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(Wholesaler_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
                
        print("Backorder:",Retailer.backorder,"On Delivery:",Retailer.on_delivery,
              "Present Cost:",-1*Retailer.cost,"Present Inventory:",Present_inventory)
        #발주 해야하는 양
        Retailer.Order()
        
        
    else:
        Retailer.Incoming_delivery(Wholesaler_df.loc[x-2][-3])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(abs(round(np.random.randn(1)[0]*10)))
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(Wholesaler_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        print("Backorder:",Retailer.backorder,"On Delivery:",Retailer.on_delivery,
              "Present Cost:",-1*Retailer.cost,"Present Inventory:",Present_inventory)
        #발주 해야하는 양
        Retailer.Order()
        
        #업데이트
    
     
    temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
    #DataFrame에 추가
    Retailer_df.iloc[x]=temp
        
 
    return Retailer_df,Present_inventory

def Wholesaler_Env(x,Retailer,Retailer_df,Present_inventory,df,Distributer_df):
    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        first_inventory=random.randint(0, 10)
        Retailer.Inventory=(first_inventory)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        #발주 해야하는 양
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        #업데이트
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        #DataFrame에 추가
        Retailer_df.iloc[x]=temp
        
        #Inventory 업데이트
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
    
    elif x==1:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(0)
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.iloc[x]=temp
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    elif x==2:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(Distributer_df.loc[x-2][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.iloc[x]=temp
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    else:
        Retailer.Incoming_delivery(Distributer_df.loc[x-2][-3])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(Distributer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.iloc[x]=temp
        Present_inventory=max(Retailer.available-Retailer.total_order,0)

    return Retailer_df,Present_inventory


def Distributer_Env(x,Retailer,Retailer_df,Present_inventory,Wholesaler_df,Manufacture_df):

    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        first_inventory=random.randint(0, 10)
        Retailer.inventory(first_inventory)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        #발주 해야하는 양
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        #Inventory 업데이트
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    elif x==1:
        Retailer.Incoming_delivery(0)

        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Wholesaler_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(Retailer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        
    elif x==2:
        Retailer.Incoming_delivery(0)

        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Wholesaler_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(Manufacture_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)

        
    else:
        Retailer.Incoming_delivery(Manufacture_df.loc[x-2][-3])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Wholesaler_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(Manufacture_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    Retailer_df.iloc[x]=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                   Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                   abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]

    return Retailer_df,Present_inventory

def Manufacturer_Env(x,Retailer,Retailer_df,Present_inventory,Distributer_df):

    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        first_inventory=random.randint(0, 10)
        Retailer.Inventory=(first_inventory)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        #발주 해야하는 양
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        #업데이트
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        #DataFrame에 추가
        Retailer_df.iloc[x]=temp
        
        #Inventory 업데이트
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
    
    
    elif x==1:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Distributer_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(0)
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.iloc[x]=temp
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    elif x==2:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Distributer_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(Distributer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.iloc[x]=temp
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    else:
        Retailer.Incoming_delivery(Retailer_df.loc[x-2][-1])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Distributer_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=abs(round(np.random.randn(1)[0]*10))
        
        Retailer.On_delivery(Distributer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.iloc[x]=temp
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
    return Retailer_df,Present_inventory

def main():
    Retailer=Table()
    Wholesaler=Table()
    Distributer=Table()
    Manufacture=Table()
    print("진행시킬 게임의 총 주를 입력하시오:")
    Total_Weeks=int(input())
    Retailer_df=np.zeros((Total_Weeks,10))
    Retailer_df=pd.DataFrame(Retailer_df)
    Retailer_df.columns=['Incoming_delivery','Inventory','available',
                         'Incoming_order','Backorder','Total_order',
                         'Cost','Delivery','Your_delivery','Your_order']

    Wholesaler_df=np.zeros((Total_Weeks,10))
    Wholesaler_df=pd.DataFrame(Wholesaler_df)
    Wholesaler_df.columns=['Incoming_delivery','Inventory','available',
                         'Incoming_order','Backorder','Total_order',
                         'Cost','Delivery','Your_delivery','Your_order']

    Distributer_df=np.zeros((Total_Weeks,10))
    Distributer_df=pd.DataFrame(Distributer_df)
    Distributer_df.columns=['Incoming_delivery','Inventory','available',
                         'Incoming_order','Backorder','Total_order',
                         'Cost','Delivery','Your_delivery','Your_order']

    Manufacture_df=np.zeros((Total_Weeks,10))
    Manufacture_df=pd.DataFrame(Manufacture_df)
    Manufacture_df.columns=['Incoming_delivery','Inventory','available',
                         'Incoming_order','Backorder','Total_order',
                         'Cost','Delivery','Your_delivery','Your_order']


    Present_Retailer_Inventory=0
    Present_Wholesaler_Inventory=0
    Present_Distributer_Inventory=0
    Present_Manufacturer_Inventory=0
    
    for x in range(Total_Weeks):
        Current_week=x+1
        print("현재 주 수:",Current_week)
        Manufacture_df,Present_Manufacturer_Inventory=Manufacturer_Env(x,Manufacture,Manufacture_df,Present_Manufacturer_Inventory,Distributer_df)
        Distributer_df,Present_Distributer_Inventory=Distributer_Env(x,Distributer,Distributer_df,Present_Distributer_Inventory,Wholesaler_df,Manufacture_df)
        Wholesaler_df,Present_Wholesaler_Inventory=Wholesaler_Env(x,Wholesaler,Wholesaler_df,Present_Wholesaler_Inventory,Retailer_df,Distributer_df)
        Retailer_df,Present_Retailer_Inventory=Retailer_Env(x,Retailer,Retailer_df,Present_Retailer_Inventory,Wholesaler_df)
        
    Manufacture_df.to_excel('M.xlsx')
    Distributer_df.to_excel('D.xlsx')
    Wholesaler_df.to_excel('W.xlsx')
    Retailer_df.to_excel('R.xlsx')
    
    
main()
